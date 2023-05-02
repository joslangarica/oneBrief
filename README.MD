
1. Install `virtualenv` if it's not installed already:

```bash
pip install virtualenv
```

2. Create a virtual environment in your project's root directory:

```bash
virtualenv venv
```

3. Activate the virtual environment:

- On Mac/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
.\venv\Scripts\activate
```

4. Now, install the required packages in the virtual environment:

```bash
pip install Flask openai python-dotenv
```

5. Run your Flask app in the virtual environment:

```bash
python app.py
```

By using a virtual environment, you can ensure that the required packages are installed in the correct environment, and it won't interfere with your system's or other projects' dependencies.