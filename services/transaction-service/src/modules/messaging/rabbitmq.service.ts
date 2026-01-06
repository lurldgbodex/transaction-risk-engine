import * as amqp from 'amqplib';
import { Logger } from '@nestjs/common';

export class RabbitMQService {
  private channel;
  private connection: amqp.Connection;
  private readonly logger = new Logger(RabbitMQService.name);

  async connect() {
    if (this.channel) return;

    this.connection = await amqp.connect(
      process.env.RABBITMQ_URL || 'amqp://localhost',
    );
    this.channel = await this.connection.createChannel();

    this.logger.log('Connected to RabbitMQ');
  }

  async publish(queue: string, message: any) {
    await this.channel.assertQueue(queue, { durable: true });

    this.channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)), {
      persistent: true,
    });
  }
}
