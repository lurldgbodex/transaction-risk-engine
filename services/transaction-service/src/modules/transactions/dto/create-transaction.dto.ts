import {
  IsUUID,
  IsEnum,
  IsNumber,
  IsPositive,
  IsString,
  IsIP,
} from 'class-validator';

export enum TransactionType {
  PAYMENT = 'payment',
  TRANSFER = 'transfer',
}

export enum Channel {
  MOBILE = 'mobile',
  WEB = 'web',
}

export class MetadataDto {
  @IsString()
  deviceId: string;

  @IsIP()
  ipAddress: string;

  @IsString()
  country: string;
}

export class CreateTransactionDto {
  @IsUUID()
  userId: string;

  @IsNumber()
  @IsPositive()
  amount: number;

  @IsString()
  currency: string;

  @IsEnum(TransactionType)
  transactionType: TransactionType;

  @IsEnum(Channel)
  channel: Channel;

  metadata: MetadataDto;
}
