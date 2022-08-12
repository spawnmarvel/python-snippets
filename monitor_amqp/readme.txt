
http://localhost:15671/api/index.html

RabbitMQ Management HTTP API

Introduction

Apart from this help page, all URIs will serve only resourcesof type application/json, and will require HTTP basicauthentication (using the standard RabbitMQ user database). Thedefault user is guest/guest.

Many URIs require the name of a virtual host as part of thepath, since names only uniquely identify objects within a virtualhost. As the default virtual host is called "/", thiswill need to be encoded as "%2F".

PUTing a resource creates it. The JSON object you upload musthave certain mandatory keys (documented below) and may haveoptional keys. Other keys are ignored. Missing mandatory keysconstitute an error.

Since bindings do not have names or IDs in AMQP we synthesiseone based on all its properties. Since predicting this name ishard in the general case, you can also create bindings by POSTingto a factory URI. See the example below.

Many URIs return lists. Such URIs can have the query stringparameters sort and sort_reverseadded. sort allows you to select a primary field tosort by, and sort_reverse will reverse the sort orderif set to true. The sort parameter cancontain subfields separated by dots. This allows you to sort by anested component of the listed items; it does not allow you tosort by more than one field. See the example below.

You can also restrict what information is returned per itemwith the columns parameter. This is a comma-separatedlist of subfields separated by dots. See the example below.

Most of the GET queries return many fields perobject. The second part of this guide covers those.

