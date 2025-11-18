exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      status: 'healthy',
      message: 'JavaScript function working on Netlify',
      platform: 'Netlify Functions'
    })
  }
}
