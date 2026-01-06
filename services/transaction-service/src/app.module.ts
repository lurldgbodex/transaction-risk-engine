import { Module } from '@nestjs/common';
import { TransactionsModule } from './modules/transactions/transactions.module';

@Module({
  imports: [],
  controllers: [],
  providers: [TransactionsModule],
})
export class AppModule {}
