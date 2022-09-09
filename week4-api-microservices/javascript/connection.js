// THIS FILE WILL BE OVERWRITTEN. DO NOT MAKE ANY CHANGES
const cassandra = require("cassandra-driver");

// This is the Zip file you downloaded
const SECURE_CONNECT_BUNDLE =
  "/workspace/bootcamp-fullstack-apps-with-cassandra/secure-connect-workshops.zip";
// This is the "Client Id" value you obtained earlier
const USERNAME = "sPxAFZKmjlqYMZIeGvlmMhfo";
// This is the "Client Secret" value you obtained earlier
const PASSWORD = "Nob,bS,9HX.e1Hj+2q.2FH4M4wUtFUvx-8l-tyYK6Wk,wb0zc3A-K7,T8.spPll7jESY5_f1hCUc46ijy8yByFTn5d94k3JBKX96WewOe.5Jf+_RiedYNdR4eloICWBY";
// This is the keyspace name
const KEYSPACE = "todos";

const client = new cassandra.Client({
  cloud: { secureConnectBundle: SECURE_CONNECT_BUNDLE },
  keyspace: KEYSPACE,
  credentials: { username: USERNAME, password: PASSWORD },
});

process.on("exit", () => client.shutdown());

module.exports = {
  client,
};
