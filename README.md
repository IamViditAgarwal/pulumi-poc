## Pulumi POC
---
Repo created for doing the POC for the Pulumi IAC Tool

## Steps Followed
* We are authenticating the pulumi with the gcp in the non-interactive manner using the IAM Service account approach . Created the custom service account and have generated the json keys for the same .

* After successfull generation of the keys , download tha keys for local testing

* Install the pulumi cli. Follow the [document](https://www.pulumi.com/docs/get-started/install/)

  * Install it from the package manager , Manual installation will result in error (Non verfified installation error)

  * To verify the installation : Run : `pulumi version`

* Signup in Pulumi web account : Link : [SignUp](https://app.pulumi.com/)

  * For now , i HAVE singed up with my personal accounts

  * After signup / login , create a token & save it . This token will be used for running and authenticating the pulumi cli with the pulumi account

* Open terminal, 

  * Createa an empty directory, navigate into it

  * Run: `pulumi new gcp-python` 

    * here : `gcp-python` is the name of the template that we will be using : it has following 2 meanings: 1. We are deploying our resource on GCP 2. We are using Python lang to code out
  
    * Fill out the details like project name , project description , stack name and google cloud project name (gcp project is the project in which the resources will be created)
  
  * Export the downloaded service account to make sure pulumi uses that for google auth

    * Run cmd: `export GOOGLE_CREDENTIALS=$(cat <creds-filename>.json)`
    
  * Run: `pulumi up` to apply the configuration i.e. create the resources

    *  Above command will create a stack under the mentioned project.



  






