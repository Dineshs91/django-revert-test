# django-revert-test
Testing revert strategies in django

## Test

Run tests with this command

`python manage.py test --keepdb`

### Branch `Master` has the following models.

Post
- title
- description
- created_at
- updated_at

Comment
- text
- post
- created_at
- updated_at

### Branch `non-destructive` has the following.

Post
- title
- description
- tags (Added field with null=True)
- created_at
- updated_at

Comment
- text
- post
- created_at
- updated_at

### Branch `destructive` has the following

Post
- title
- ~~description~~ (Field removed)
- created_at
- updated_at

Comment
- text
- post
- created_at
- updated_at

## Reset the database

Use this command to reset the database.

`python manage.py reset_db`

**Note:** This command is available from `django-extensions` package.

## References
http://lucasroesler.com/2017/02/zero-downtime-deploys-a-tale-of-django-migrations/
