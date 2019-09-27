# Tickets Back

This project is a simplification from the presentation made by [Carlos Martinez](https://github.com/CarlosMart626)
@ [DjangoCon US 2019](https://2019.djangocon.us/) Original code in [this repo](https://github.com/CarlosMart626/djangocon-2019)

Docker deploy based on [Contraslash Django Deploy Common for postgres](https://hub.docker.com/r/contraslash/alpine-django-deploy-common-postgres)

To build and test locally:

```bash
docker build -t contraslash/ops_with_actions_back .
docker run \
  -p 8000:8000 \
  contraslash/ops_with_actions_back

```