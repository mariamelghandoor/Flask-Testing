import unittest
from task4 import app, get_tasks, add_task, add_task_route

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_tasks(self):
        tasks = get_tasks()
        self.assertEqual(len(tasks) >= 0 , True)
    
    def test_add_task(self):
        tasks = add_task('Buy groceries')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], 'Buy groceries')
    
    def test_integrated_get_and_add(self):
        tasks = get_tasks()
        lenght = len(tasks)
        # add twice
        add_task('Buy groceries')
        add_task('Clean the house')
        tasks = get_tasks()
        # check for their existance 
        self.assertEqual(len(tasks) >= 2, True)
        self.assertEqual(tasks[lenght], 'Buy groceries')
        self.assertEqual(tasks[lenght+1], 'Clean the house')
    
    def test_integrated_test_add_task_with_route(self):
        response = self.app.post('/add_task', data={'task': 'Buy groceries'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buy groceries', response.data)

    def test_integrated_route_get_and_add(self):
        # add two tasks
        response = self.app.post('/add_task', data={'task': 'Buy groceries'})
        self.assertEqual(response.status_code, 200)
        
        response = self.app.post('/add_task', data={'task': 'Clean the house'})
        self.assertEqual(response.status_code, 200)

        # check for their existance
        response = self.app.get('/')
        self.assertIn(b'Buy groceries', response.data)  
        self.assertIn(b'Clean the house', response.data)


if __name__ == '__main__':
    unittest.main()
