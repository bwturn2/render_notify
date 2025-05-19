import express from 'express';
import { supabase } from '../services/supabaseClient.js';

const router = express.Router();

router.post('/', async (req, res) => {
  const { user_id, payload } = req.body;

  const { error } = await supabase
    .from('logs')
    .insert([{ user_id, payload }]);

  if (error) {
    console.error(error);
    return res.status(500).json({ error: error.message });
  }

  res.status(200).json({ message: 'Webhook received and logged.' });
});

export default router;
