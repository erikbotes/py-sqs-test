Simple Python tool to play with SQS

####Installing an running:
1. Have Python, pip and virtualenv installed
21. Clone the repo
3. Settings:
3.1 Export `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables
3.2 Edit `settings.py` to contain your queue URL.
4. Create a virtual environment:
`$ virtualenv --no-site-packages venv`
5. Activate your new virtualenv:
`$ source venv/bin/activate`
6. Run Python in interactive mode with the script:
`$ python -i sqs.py`


####Example run:

```python
send("Hello World!")
>>> <some message id>
receive()
>>> "Hello World!"
>>> <receipt_handle for this message>
delete(receipt_handle)
>>> Deleted!
```
