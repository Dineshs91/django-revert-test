# django-revert-test
Testing revert strategies in django

## Test

Run tests with this command

`python manage.py test --keepdb`

Branch `Master` has the following models.

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

## References
http://lucasroesler.com/2017/02/zero-downtime-deploys-a-tale-of-django-migrations/
