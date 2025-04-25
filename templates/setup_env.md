# Set Up Environment Variables

To configure the application, you need to set up the following environment variables:

## 1. SECRET_KEY
This is a secret key used by Flask for session management and other security-related features. You can generate a random secret key using Python:

```bash
python3 -c 'import secrets; print(secrets.token_hex(16))'
```

Use the generated key in the following command:

```bash
export SECRET_KEY="your-generated-secret-key"
```

## 2. DATABASE_URI
This is the URI for the database. By default, the application uses SQLite. If you want to use SQLite, you can set it as follows:

```bash
export DATABASE_URI="sqlite:///projects.db"
```

If you are using another database (e.g., PostgreSQL, MySQL), replace the URI with the appropriate connection string. For example:

- PostgreSQL:
  ```bash
  export DATABASE_URI="postgresql://username:password@localhost/dbname"
  ```

- MySQL:
  ```bash
  export DATABASE_URI="mysql+pymysql://username:password@localhost/dbname"
  ```

## Steps to Set Environment Variables
1. Open your terminal.
2. Run the `export` commands shown above to set the variables.
3. To make these variables persistent, add them to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`).
4. Restart your terminal or run `source ~/.bashrc` (or `source ~/.zshrc`).

Once these variables are set, the application will use them during runtime.