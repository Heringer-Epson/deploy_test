# Test template to deploy Dash on Google Cloud

###This app builds on [this](https://www.phillipsj.net/posts/deploying-dash-to-google-app-engine/) example.

1) ~/> python3 -m venv .venvs/test_env
2) ~/source .venvs/test_env/bin/activate
3) If not connected to git repo: Hamburger Menu -> Source repositories -> connect to external...
4) gcloud source repos clone github_heringer-epson_deploy_test deploy-test
5) cd deploy-test/
6) pip install -r requirements.txt
7) python main.py (this is a test only).
8) gcloud app deploy (actual deployment).
