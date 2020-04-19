const express = require('express');
const router = express.Router();
const db = require('./queries');

router.get('/timetable', db.getTimetableByTripId);
router.get('/users/:id', db.getUserById);

module.exports = router;