requirejs.config({
    baseUrl: "./js",
    urlArgs: "bust=" + (new Date).getTime(),
    paths: {
        temp: "../temp",
        app: "../app",
        mycss: "../../css"
    },
    waitSeconds: 0
});