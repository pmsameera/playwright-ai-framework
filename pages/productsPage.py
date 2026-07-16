import { test, expect } from '@playwright/test';

test('should open TodoMVC and add a todo', async ({ page }) => {
  // 1. Open the app
  await page.goto('https://todomvc.com/examples/react/dist/');

  // 2. Locate the input field (Todo input)
  const todoInput = page.getByPlaceholder('What needs to be done?');

  // 3. Add a todo
  await todoInput.fill('Buy milk');
  await todoInput.press('Enter');

  // 4. Assert todo appears in the list
  const todoItem = page.getByText('Buy milk');
  await expect(todoItem).toBeVisible();
});