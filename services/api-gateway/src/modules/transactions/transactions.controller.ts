import { Controller, Post, HttpCode, Body } from '@nestjs/common';
import { CreateTransactionDto } from './dto/create-transaction.dto';
import { TransactionService } from './transactions.service';

@Controller('/api/v1/transactions')
export class TransactionController {
  constructor(private readonly service: TransactionService) {}

  @Post()
  @HttpCode(202)
  async create(@Body() dto: CreateTransactionDto) {
    return this.service.forwardTransaction(dto);
  }
}
