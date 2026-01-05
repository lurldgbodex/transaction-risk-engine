import { Module } from '@nestjs/common';
import { TransactionService } from './transactions.service';
import { HttpModule } from '@nestjs/axios';
import { TransactionController } from './transactions.controller';

@Module({
  imports: [HttpModule],
  providers: [TransactionService],
  controllers: [TransactionController],
})
export class TransactionModule {}
