SELECT teacher_id, COUNT(teacher_id) AS num
FROM Teacher
GROUP BY teacher_id
