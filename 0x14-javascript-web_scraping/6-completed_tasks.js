#!/usr/bin/node
// Script to compute the number of tasks completed by user id

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Create an obj to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Filter and count completed tasks
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print users with completed tasks
    console.log(completedTasksByUser);
  }
});
