import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Transaction } from './transaction.entity';
import { TransactionService } from './transactions.service';
import { RabbitMQService } from '../messaging/rabbitmq.service';
import { TransactionController } from './transaction.controller';

@Module({
  imports: [TypeOrmModule.forFeature([Transaction])],
  providers: [TransactionService, RabbitMQService],
  controllers: [TransactionController],
})
export class TransactionsModule {}
