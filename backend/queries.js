const {pool} = require('./config');

const getTimetableByTripId = (request, response) => {
    "use strict";
    pool.query('SELECT * FROM public.timetable ORDER BY id ASC LIMIT 100', (error, results) => {
        if (error) {
            throw error;
        }
        response.status(200).json(results.rows);
    });
};

const getUserById = (request, response) => {
    "use strict";
    const id = parseInt(request.params.id);
    pool.query('SELECT * FROM users WHERE id = $1', [id], (error, results) => {
        if (error) {
            throw error;
        }
        response.status(200).json(results.rows);
    });
};

module.exports = {
    getTimetableByTripId,
    getUserById,
};