import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TransactionsModule } from './modules/transactions/transactions.module';
import { databaseConfig } from './config/database.config';

@Module({
  imports: [TypeOrmModule.forRoot(databaseConfig), TransactionsModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
