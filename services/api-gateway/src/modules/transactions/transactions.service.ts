import { HttpException, HttpStatus, Injectable } from '@nestjs/common';
import { CreateTransactionDto } from './dto/create-transaction.dto';
import { v4 as uuid } from 'uuid';
import { HttpService } from '@nestjs/axios';
import { firstValueFrom } from 'rxjs';

@Injectable()
export class TransactionService {
  constructor(private readonly httpService: HttpService) {}

  async forwardTransaction(dto: CreateTransactionDto) {
    try {
      const response = await firstValueFrom(
        this.httpService.post(
          `${process.env.TRANSACTION_SERVICE_URL || 'http://localhost:3001'}/transactions`,
          dto,
        ),
      );
      return response.data;
    } catch (error) {
      throw new HttpException(
        'Transaction service unavailable',
        HttpStatus.SERVICE_UNAVAILABLE,
      );
    }
  }
}
