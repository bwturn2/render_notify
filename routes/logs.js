import express from 'express';
import { supabase } from '../services/supabaseClient.js';

const router = express.Router();

router.get('/:userId', async (req, res) => {
  const { userId } = req.params;

  const { data, error } = await supabase
    .from('logs')
    .select('*')
    .eq('user_id', userId);

  if (error) {
    console.error(error);
    return res.status(500).json({ error: error.message });
  }

  res.status(200).json(data);
});

export default router;
