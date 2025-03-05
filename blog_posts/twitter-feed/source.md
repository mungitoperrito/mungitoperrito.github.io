# Chewing on the Twitter Feed

Twitter streams millions of messages all day long. Have you ever wanted to use
their feed to do your own analysis of streaming posts?

If so, follow along. That's what this post is about.


## Background

A few years ago, Assaf Mentzer put together a demonstration project, [Building a
Near Real-Time Discovery Platform with AWS]]
(https://aws.amazon.com/blogs/big-data/building-a-near-real-time-discovery-platform-with-aws/)
to introduce readers to streaming data. Since then AWS has made changed some of
the services he used.

This page updates Assaf’s instructions and adds a few additional tips for anyone
who wants to get started analyzing the Twitter feed.

The steps on this page extend Assaf’s post. For additional context, open Assaf’s
page in another browser tab so you can refer to his post too.

## Prerequisites

You need an AWS account and a Twitter account.

Consider creating a new Twitter account for this project instead of
reusing your usual one (if you already have one). The advantage of a new account
is that you can use different preferences and settings for this data exploration
project and you won’t have to modify your usual settings.

## Create an Amazon Elasticsearch Service cluster

### Sign in to the Elasticsearch Service Console.

1. If this is your first sign in to the Elasticsearch Console, select `Get
   Started`.

   If you have used the Elasticsearch Console before, select, `Create a New
   Domain`.

   <img src="./img/create-cluster..01.jpg" data-width="1000" data-height="579"
   alt="Create elastic search cluster">

1. Name your domain then click `Next`. This example uses: “es-twitter-demo”.
1. Assaf recommends accepting the defaults on the next screen. It is cheaper to
   use a smaller EC instance to host the elasticsearch domain. The
  `t2.medium.elasticsearch` instance type works well for simple experiments.
1. Choose `Allow Open Access` as the domain policy. This is a poor security
  practice and the console will complain about it. If you want to do more than
  simple experimentation, configure a more restrictive security policy.

  <img src="./img/access-policy..01.jpg" data-width="1000" data-height="579"
   alt="Configure access policy">

1. Choose `Confirm and Create`. It takes about 10 minutes to set up the domain.

   <img src="./img/confirm..01.jpg" data-width="1000" data-height="579"
   alt="Create domain confirmation dialog">

1. To confirm your domain configuration, click on the endpoint when it is active.

   <img src="./img/elastic-search..01.jpg" data-width="1000" data-height="579"
   alt="Elasticsearch service dashboard">

1. The service console displays configuration details for the new endpoint. Save
   this information down for later. Be sure to make a note of the Elasticsearch
   service endpoint and the Kibana URL.

   <img src="./img/console..01.jpg" data-width="1000" data-height="579"
   alt="Elasticsearch configuration details">

## Create an IAM role for Firehose

In this section, you create a role in AWS to work with the Twitter Firehouse
feed.

1. On your desktop, create two policy files.

   NOTE: If you cut and paste the configuration from original post, you may get
   hidden artifacts in the policy files. The uploads fails if the artifacts are
   there. If that happens, just retype the files manually. The syntax in the
   original article is correct.

1. Edit the `s3-rw-policy.json` file to use your S3 bucket.

   <img src="./img/iam-role..01.jpg" data-width="1000" data-height="579"
   alt="S3 configuration">

1. To upload the policy files, use the AWS CLI client.
1. Verify that the policy is in place.

   <img src="./img/iam-role..02.jpg" data-width="1000" data-height="579"
   alt="Verify access policy">

## Create a Lambda function

This section makes a lot of updates to the original post. The Lambda function
setup and the configuration process have changed considerably since Assaf's blog
post was published in 2015.

1. Download the deployment package.
1. Unzip the package to your project folder (`s3-twitter-to-es-python`).
1. Modify the `s3-twitter-to-es-python/config.py` file. Edit the file so that
   the value of `es_host` matches the Elasticsearch Service endpoint for your
   domain.

   <img src="./img/lambda..01.jpg" data-width="1000" data-height="579"
   alt="Edit config file">

1. Zip the folder content in your local environment. This example uses
   `my-s3-twitter-to-es-python.zip`

   It is important to zip the entire folder contents. Don't zip up the folder by
   itself.
1. Sign in to the Lambda console.
1. If this is your first time using Lambda, select `Get started now`.

   If you have used Lambda before, select `Create a Lambda function`.
1. Select `Configure triggers` from the list of choices at top left of the
   screen.

   <img src="./img/lambda..02.jpg" data-width="1000" data-height="579"
   alt="Configure lambda triggers">

1. To select a storage location, click inside the dotted lines and select `S3`
   from the drop down list.

   <img src="./img/lambda..03.jpg" data-width="1000" data-height="579"
   alt="Select storage location">

1. Enter your S3 bucket name. Verify that `Enable trigger` checked.

   <img src="./img/lambda..04.jpg" data-width="1000" data-height="579"
   alt="S3 bucket name">

1. Use these values to update the variables on the next screen:

   ```
   # Your project name
   Name: 's3-twitter-to-es-python

   Runtime: 'Python2.7'

   Code entry: 'Upload a .ZIP file'
   # Click the button to upload the .zip file you created earlier

   Handler: 'lambda_function.lambda_handler'

   Role: 'Create new role from templates(s)'

   Role name: 'lamdba_s3_exec_role'

   Memory: 128

   Timeout: '2 minutes'
   ```

   <img src="./img/function..01.jpg" data-width="1000" data-height="579"
   alt="Lambda function configuration">

   <img src="./img/function..02.jpg" data-width="1000" data-height="579"
   alt="Additional lambda configuration">

1. Create the function.
1. Verify that the role was created properly.

   <img src="./img/function..03.jpg" data-width="1000" data-height="579"
   alt="Verify lambda role">

1. Verify the S3 bucket has permissions set properly.

   <img src="./img/function..04.jpg" data-width="1000" data-height="579"
   alt="Verify lambda role">


## Stream data from Twitter to the producer

That’s a lot of configuration and backend set up so far, but we are nearly there. The next steps are where the fun begins. Assaf configured a fairly restrictive data feed. You can change his configuration to select tweets which you think are more interesting.</p><p name="1ccf" id="1ccf" class="graf graf--p graf-after--p">Using the suggested t2.micro instance for the node.js host works well for the demo. Be aware that the stock configuration file is limited to US data and it only sends a few of the available fields from the Twitter stream. If you really want to pull in lots of data you may want to upgrade your server instances. That said, when starting out it is probably best to stick with the standard configuration.</p><p name="fc42" id="fc42" class="graf graf--p graf-after--p">If you want to change the data streams later on, here are some tips on how to do it.</p><h3 name="a0f9" id="a0f9" class="graf graf--h3 graf-after--p">Add countries outside the US to the stream</h3><p name="ad81" id="ad81" class="graf graf--p graf-after--h3">This sends a LOT of data for the demo to process.</p><ul class="postList"><li name="ca90" id="ca90" class="graf graf--li graf-after--p">Go to the node.js host.</li><li name="ce21" id="ce21" class="graf graf--li graf-after--li">Change directory to twitter-streaming-firehose-nodejs.</li><li name="a989" id="a989" class="graf graf--li graf-after--li">Edit config.js to comment out the regional filter.</li><li name="5f61" id="5f61" class="graf graf--li graf-after--li">Restart the node server.</li></ul><figure name="1e62" id="1e62" class="graf graf--figure graf-after--li">
 class="aspectRatioPlaceholder is-locked" style="max-width: 700px; max-height: 421px;">
 class="aspectRatioPlaceholder-fill" style="padding-bottom: 60.199999999999996%;"></div><img class="graf-image" data-image-id="0*YQJYpsyoVPLdexEy.jpg" data-width="779" data-height="469" src="https://cdn-images-1.medium.com/max/800/0*YQJYpsyoVPLdexEy.jpg"></div><figcaption class="imageCaption">Edit config.js</figcaption></figure><h3 name="15a4" id="15a4" class="graf graf--h3 graf-after--figure">Add new fields to the stream</h3><p name="5d08" id="5d08" class="graf graf--p graf-after--h3">That was a great start, but you are probably anxious to gather other types of meta data. You can increase the amount of data collected in each Tweet by modifying the Lambda Function. Here’s how:</p><ul class="postList"><li name="2ba8" id="2ba8" class="graf graf--li graf-after--p">Go to the s3-twitter-to-es-python directory.</li><li name="b559" id="b559" class="graf graf--li graf-after--li">Edit tweet_utils.py to add additional fields in the get_tweets() function.</li><li name="1fd3" id="1fd3" class="graf graf--li graf-after--li">Rob Johnson has compiled a list of <a href="https://gist.github.com/robjohnson/702360" data-href="https://gist.github.com/robjohnson/702360" class="markup--anchor markup--li-anchor" rel="noopener" target="_blank">available fields</a>.</li></ul><figure name="42d7" id="42d7" class="graf graf--figure graf-after--li">
 class="aspectRatioPlaceholder is-locked" style="max-width: 696px; max-height: 438px;">
 class="aspectRatioPlaceholder-fill" style="padding-bottom: 62.9%;"></div><img class="graf-image" data-image-id="0*BFlqwL1zSJLdlm08.jpg" data-width="696" data-height="438" src="https://cdn-images-1.medium.com/max/800/0*BFlqwL1zSJLdlm08.jpg"></div><figcaption class="imageCaption">Adding data fields</figcaption></figure><ul class="postList"><li name="b2b9" id="b2b9" class="graf graf--li graf-after--figure">Zip up the directory again</li><li name="9426" id="9426" class="graf graf--li graf-after--li">Go to your function in the Lambda Management console.</li><li name="6d57" id="6d57" class="graf graf--li graf-after--li">Upload the new .zip file. It will replace the old function.</li><li name="535c" id="535c" class="graf graf--li graf-after--li">Go to the monitoting tab.</li><li name="ff9b" id="ff9b" class="graf graf--li graf-after--li">Click on ‘View logs in CloudWatch’ to verify the new function works properly. These logs are very useful to debug any errors in the python script.</li></ul><figure name="970d" id="970d" class="graf graf--figure graf-after--li">
 class="aspectRatioPlaceholder is-locked" style="max-width: 700px; max-height: 331px;">
 class="aspectRatioPlaceholder-fill" style="padding-bottom: 47.3%;"></div><img class="graf-image" data-image-id="0*fMJoc0nuxITV8CiJ.jpg" data-width="1000" data-height="473" src="https://cdn-images-1.medium.com/max/800/0*fMJoc0nuxITV8CiJ.jpg"></div><figcaption class="imageCaption">View console activity</figcaption></figure><h3 name="ab7b" id="ab7b" class="graf graf--h3 graf-after--figure">Add new indices to Kibana</h3><p name="2040" id="2040" class="graf graf--p graf-after--h3">Kibana helps you to aggregate your data. When working with different data sets it may be useful to add another index or two to segregate your information streams. You can do it like this:</p><ul class="postList"><li name="f235" id="f235" class="graf graf--li graf-after--p">Go to the s3-twitter-to-es-python directory.</li><li name="6b62" id="6b62" class="graf graf--li graf-after--li">Edit twitter_to_es.py to update the index name.</li></ul><figure name="75ca" id="75ca" class="graf graf--figure graf-after--li">
 class="aspectRatioPlaceholder is-locked" style="max-width: 535px; max-height: 94px;">
 class="aspectRatioPlaceholder-fill" style="padding-bottom: 17.599999999999998%;"></div><img class="graf-image" data-image-id="0*c_WJVk4OI0Ukh6uZ.jpg" data-width="535" data-height="94" src="https://cdn-images-1.medium.com/max/800/0*c_WJVk4OI0Ukh6uZ.jpg"></div><figcaption class="imageCaption">Add an new index</figcaption></figure><ul class="postList"><li name="b598" id="b598" class="graf graf--li graf-after--figure">Zip up the directory again</li><li name="0529" id="0529" class="graf graf--li graf-after--li">Go to your function in the Lambda Management console.</li><li name="df14" id="df14" class="graf graf--li graf-after--li">Upload the new .zip file. You will see the new index listed on the ‘Indices’ tab for for ElasticSearch domain.</li></ul><h3 name="9a2f" id="9a2f" class="graf graf--h3 graf-after--li">Discover and analyze data</h3><p name="1f55" id="1f55" class="graf graf--p graf-after--h3">The tweet data is transferred to the S3 bucket you configured every 5 minutes or when it reaches a particular size. Depending on how much data you decided to capture, you should start to see data files appearing in S3 very soon. Once the first data item appears in S3, the Lambda function should process it.</p><p name="a028" id="a028" class="graf graf--p graf-after--p">The first processing iteration should happen in about five minutes. If you don’t see any output from the lambda function, first verify that data is being written to S3. Then check that the S3 bucket permissions are correct for reading. It is ok to open the bucket permissions to be world readable since the bucket only holds publicly available data anyway. NOTE: You should choose more restrictive access permissions for more sensitive data.</p><p name="04dc" id="04dc" class="graf graf--p graf-after--p">When ElasticSearch confirmed your domain above, a URL was created for Kibana. Don’t be disappointed if the URL didn’t link to anything interesting then. Kibana won’t return anything until after the Lambda function has processed the first set of data. Once that happens you are free to explore!</p><h3 name="5e86" id="5e86" class="graf graf--h3 graf-after--p graf--trailing">Happy tweet prospecting!</h3></div></div></section>
</section>
<footer><p>By <a href="https://medium.com/@dave.cuthbert" class="p-author h-card">Dave Cuthbert</a> on <a href="https://medium.com/p/4fce463790f9"><time class="dt-published" datetime="2019-01-09T06:16:00.766Z">January 9, 2019</time></a>.</p><p><a href="https://medium.com/@dave.cuthbert/chewing-the-twitter-feed-with-aws-4fce463790f9" class="p-canonical">Canonical link</a></p><p>Exported from <a href="https://medium.com">Medium</a> on April 12, 2019.</p></footer></article></body></html>