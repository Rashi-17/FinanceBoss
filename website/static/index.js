function deleteGoal(goalId) {
    fetch("/delete-goal", {
      method: "POST",
      body: JSON.stringify({ goalId: goalId }),
    }).then((_res) => {
      window.location.href = "/per_goals";
    });
  }