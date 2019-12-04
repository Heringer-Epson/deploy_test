---
# Deploying a DASH app on the cloud.
---

---
#### Acronyms:
+ HB: Hamburger Menu on Google Cloud.
+ VM: Virtual Machine. 
+ GCP: Google Cloud Platform.
+ GCS: Google Cloud Shell.
---

---
#### Example:
+ Link to an example of Dash app: https://github.com/Heringer-Epson/deploy_test
---

---
#### Instructions:

+ Create new project (e.g. myproj-test)
+ Create VM instance
  + HB -> Compute Engine -> VM instances
    + Ubuntu 18.04 LTS
    + 100 GB
    + allow HTTP and HTTPS
+ Set Firewall rules
  + Detailed instructions (here)[https://docs.bitnami.com/google/faq/administration/use-firewall/]
  + HB -> VPC Network -> Firewall rules
    + Create Firewall rule.
    + Leave all default, except the following. 
    + Targets: All instances
    + Source IP ranges: 0.0.0.0/0
    + tcp: 8080
    + Note: This should prevent bad gateway errors.
+ Set static IP address
  + HB -> VPC Network -> Set External IP addresses.
  + Reserve static IP address. Attach it to the project.
+ If using a project from Github.
  + Link the GCP to your git repo.
    + HB -> Source repositories.
    + On the top right, click Add repository.
    + Connect to external repo (naviagate through the options).
    + You may need to add an ssh key to git (not entirely sure). If so, see (this link)[https://cloud.google.com/source-repositories/docs/authentication#ssh].
    + If needed, more instructions can be found (here)[https://www.youtube.com/watch?v=D85bCIvPM1s].
+ Naviagte to your GCP project and start a GCS (terminal icon on top right).
  + ls (see the content of the home dir. The git repo should be there. If not, try:
  + gcloud source repos clone "REPOSITORY_NAME" "DIRECTORY_NAME"
+ OPTION 1) Test your app.
  + This is a way to test your app before deploying it. It can save a lot of debugging time.
  + On the home dir, create and activate a virtual env:
    + python3 -m venv .venvs/test_env
    + source .venvs/test_env/bin/activate
  + Switch to the repo dir and install the package requirements:
    + cd "REPO DIR".
    + pip install -r requirements.txt
  + Run app.
    + python main.py
  + (This source)[https://www.phillipsj.net/posts/deploying-dash-to-google-app-engine/] by Jamie Phillips is great! 
+ OPTION 2) Deploy the app.
  + A Note: when an app is deployed, a 'Docker' container is created. This is similar to a virtual env. Instructions on how to create this container are passed through a app.yaml file. App that only use python mative packages are somewhat easy to deploy, as a default container will suffice.
  + In the repo dir, simply type:
    + gcloud app deploy --stop-previous-version
  + If something goes wrong and you need to debug your deployed code, try:
    + gcloud app logs tail -s default
+ If you try too many times to deploy an app, GCP might compain that you have exceed your quota. Run the following:
  + gcloud app versions list | grep -v SERVING | awk '{print $2}' | tail -n +1 | xargs -I {} gcloud app versions delete {} 
+ Useful resources:
  + https://www.phillipsj.net/posts/deploying-dash-to-google-app-engine/
  + https://www.youtube.com/watch?v=RbejfDTHhhg
  + https://www.youtube.com/watch?v=QUYCiIkzZlA

---
