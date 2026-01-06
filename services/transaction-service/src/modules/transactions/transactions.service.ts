import { Injectable, Logger } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Transaction } from './transaction.entity';
import { Repository } from 'typeorm';
import { RabbitMQService } from '../messaging/rabbitmq.service';
import { v4 as uuidv4 } from 'uuid';
import { CreateTransactionDto } from './dto/create-transaction.dto';

@Injectable()
export class TransactionService {
  private readonly logger = new Logger(TransactionService.name);

  constructor(
    @InjectRepository(Transaction)
    private readonly transactionRepository: Repository<Transaction>,
    private readonly rabbitMQService: RabbitMQService,
  ) {}

  async onModuleInit() {
    await this.rabbitMQService.connect();
  }

  async createTransaction(dto: CreateTransactionDto) {
    const transaction = this.transactionRepository.create({
      id: uuidv4(),
      userId: dto.userId,
      amount: dto.amount,
      currency: dto.currency,
      channel: dto.channel,
      status: 'PENDING_RISK_EVALUATION',
    });

    await this.transactionRepository.save(transaction);

    const event = {
      eventId: uuidv4(),
      eventType: 'TRANSACTION_CREATED',
      timestamp: new Date().toISOString(),
      payload: {
        transactionId: transaction.id,
        userId: transaction.userId,
        amount: transaction.amount,
        currency: transaction.currency,
        transactionType: dto.transactionType,
        channel: transaction.channel,
        country: dto.metadata?.country,
      },
    };

    await this.rabbitMQService.publish('transaction.created', event);

    this.logger.log(
      `Transaction created and event published: ${transaction.id}`,
    );

    return {
      transactionId: transaction.id,
      status: transaction.status,
    };
  }
}
