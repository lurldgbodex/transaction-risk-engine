import { Body, Controller, HttpCode, Post } from '@nestjs/common';
import { TransactionService } from './transactions.service';
import { CreateTransactionDto } from './dto/create-transaction.dto';

@Controller('transactions')
export class TransactionController {
  constructor(private readonly service: TransactionService) {}

  @Post()
  @HttpCode(202)
  async create(@Body() dto: CreateTransactionDto) {
    return this.service.createTransaction(dto);
  }
}
