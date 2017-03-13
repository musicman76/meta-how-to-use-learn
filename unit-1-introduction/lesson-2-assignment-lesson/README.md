# Assignment Lesson

An assignment lesson is basically a practical programming exercise. Learn supports code execution, so you have to solve and submit the assignment through this very same platform. You can see a real example of an assignment of our [Introduction to Python Programming online course](https://rmotr.com/introduction-to-python-programming), for example: [Remove Duplicates](http://learn.rmotr.com/python/introduction-to-programming-with-python/collections-advanced/remove-duplicates).

## Understanding the requirements

Each assignment lesson will have a human readable description of what we're expecting you to do.

The assignment lesson also has tests (TDD) that we run to check the execution of your code. You can see those tests in the _Tests_ tab:

![image](https://cloud.githubusercontent.com/assets/872296/23874417/54624f68-0814-11e7-8890-ae5ae1ed027c.png)

**Tests are really important**, as they'll let you make more sense out of the requirements of the exercise. For example, in that exercise you can see a line similar to this one:

```python
self.assertEqual(
    remove_duplicates([1, 1, 1, 1, 1, 3, 4, 5, 5, 5]),  # we expect this, to be equals to:
    [1,3,4,5]                                           # < this
)
```

In this case we're expecting that, if we pass the list `[1, 1, 1, 1, 1, 3, 4, 5, 5, 5]` to your `remove_duplicates` function, you remove all duplicate numbers and return `[1,3,4,5]`.

Once you write your code, you can submit it and see the result of your assignment.

![image](https://cloud.githubusercontent.com/assets/872296/23874252/a85e428a-0813-11e7-9f22-3cc513488626.png)

If your submission contains errors, you'll see something like this in your screen:

![image](https://cloud.githubusercontent.com/assets/872296/23874311/dee01266-0813-11e7-96ad-87ebd3df8dc1.png)

![image](https://cloud.githubusercontent.com/assets/872296/23874315/e65084a4-0813-11e7-939e-6fdf7f2f6e50.png)

After all the tests pass, you'll complete the lesson and it'll be marked as done in the left menu:

![image](https://cloud.githubusercontent.com/assets/872296/23875023/ada36006-0816-11e7-9622-2be0ae31abeb.png)
