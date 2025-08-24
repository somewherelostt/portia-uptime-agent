module.exports = (req, res) => {
  // Intentionally return a 500 error for Portia testing
  res.status(500).json({
    error: "Website intentionally down for Portia Uptime Agent testing",
    message: "This error is expected - Portia should detect and fix this",
  });
};
