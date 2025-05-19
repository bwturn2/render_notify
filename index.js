import dotenv from 'dotenv';
dotenv.config();

console.log('[ENV CHECK] SUPABASE_URL =', process.env.SUPABASE_URL);

import express from 'express';
import cors from 'cors';

import webhookRoutes from './routes/webhook.js';
import logRoutes from './routes/logs.js';

const app = express();

app.use(cors());
app.use(express.json());

app.use('/webhook', webhookRoutes);
app.use('/logs', logRoutes);

app.get('/', (req, res) => res.send('RenderNotify API is live.'));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
