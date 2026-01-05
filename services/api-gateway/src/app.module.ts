import { Module } from '@nestjs/common';
import { TransactionModule } from './modules/transactions/transactions.module';

@Module({
  imports: [TransactionModule],
  providers: [],
})
export class AppModule {}
