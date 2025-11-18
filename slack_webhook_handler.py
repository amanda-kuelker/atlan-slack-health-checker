if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    print("🚀 Starting Atlan Health Check App...")
    print(f"✅ Webhook server running on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
