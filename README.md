# Getting started

## Oauth
To work, you will have to setup the oauth config for the extension. Follow [this](https://medium.com/geekculture/googles-oauth2-authorization-with-chrome-extensions-2d50578fc64f) article and put the relevant values in the **provider** manifest.json. You will also want to set the provider id at the top of test-app/client.js


## Dictionaries
If you want to test language models (for example the google docs training), you will have to generate the dictionaries for encoding words. To do that, run gen_dicts.py.<br>
``` python3 gen_dicts.py ```

You can modify lim_num_words at the top of gen_dicts.py to limit the size of the model vocabulary (for performance). This is not a great design for language models in general, however it is impossible to know the vocabulary of the model since the docs being trained on could contain anything. To my knowledge, there is not a great way to work with arbitrary model vocabularies besides just choosing a subset of common words in the langauge and ignoring everything else.

## Building and using the extension
Both directories provider and test-app support  ```yarn watch``` and ```yarn build```. Build them before doing anything else

Follow [this](https://developer.chrome.com/docs/extensions/mv3/getstarted/) link to add the extensions to your chrome browser


# Design
Provider works by listening for messages from other extensions. The messages contain serialized versions of the models the extensions want trained, as well as parameters for what training to do (data source, timesteps for sequential data, sizes for image data, etc). Provider then trains the model and sends a serialized version of the updated model back to the extension that made the request. The requesting extension receives an updated model without having seen the data provider trained it on.

# Next steps
More use cases. It is difficult to find useful applications of training on data you can never see.<br>
<br>
Expand upon test-app client to support exporting model deltas rather than the entire model.