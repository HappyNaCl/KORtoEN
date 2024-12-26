export default {
  server: {
    proxy: {
      "/ocr": {
        target: "http://localhost:5000",
        changeOrigin: true,
        secure: false,
      },
    },
  },
};
