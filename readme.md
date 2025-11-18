# Atlan Slack Health Checker - Professional Data Governance Assessments

A professional Flask application that integrates with Slack to provide instant Atlan data governance health assessments using real MCP (Model Context Protocol) integration.

## 🚀 **FIXED: Canvas Assessments Now Delivered to Slack!**

The key issue was that Canvas assessments were only being printed to console logs. **This version now sends the complete professional Canvas assessment back to Slack!**

## Features

✅ **Real Atlan MCP Integration** - Fetches live data from Atlan tenants
🏥 **Professional Health Scoring** - Industry-specific governance assessments  
📊 **Canvas-Style Deliverables** - Client-ready assessment documents **DELIVERED TO SLACK**
🎯 **Industry-Specific Analysis** - Finance, Healthcare, Construction, Retail, Technology, Manufacturing
💰 **ROI Projections** - Business impact calculations and roadmaps
🔄 **Smart Chunking** - Handles long Canvas assessments by splitting into multiple Slack messages

## Quick Start

### 1. Deploy to Vercel

```bash
# Clone and deploy
git clone <your-repo>
cd atlan-slack-health-checker
vercel deploy --prod
```

### 2. Configure Slack App

**Request URL:** `https://your-app-name.vercel.app/slack/atlan-setup`
**Command:** `/atlan-health`
**Method:** POST

### 3. Test the Integration

```bash
# Test the API directly
python3 test_slack_integration.py

# Or use curl
curl -X POST https://your-app-name.vercel.app/slack/atlan-setup \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'text=TechCorp https://dsm.atlan.com industry:technology tags:Finance&user_name=testuser&channel_name=general'
```

### 4. Use in Slack

```bash
# Technology company with dsm.atlan.com
/atlan-health "TechCorp" https://dsm.atlan.com industry:technology tags:Finance

# Healthcare company
/atlan-health "Regional Hospital" https://dsm.atlan.com industry:healthcare connections:snowflake

# Finance company  
/atlan-health "MegaBank Corp" https://bank.atlan.com industry:finance tags:SOX,PII
```

## 🔧 **What Was Fixed**

### Before (Issue):
- ✅ Slack command worked
- ✅ Real MCP data fetching worked  
- ✅ Canvas assessment generated
- ❌ **Canvas only printed to console/logs**
- ❌ **No deliverable sent back to Slack**

### After (Fixed):
- ✅ Slack command works
- ✅ Real MCP data fetching works
- ✅ Canvas assessment generated
- ✅ **Canvas automatically sent back to Slack**
- ✅ **Smart chunking for long assessments**
- ✅ **Error handling with Slack notifications**

## Canvas Delivery Features

🔄 **Smart Chunking**: Long Canvas assessments are automatically split into multiple Slack messages (max ~4000 chars each)

📋 **Professional Formatting**: Canvas assessments delivered with proper formatting using Slack code blocks

⚡ **Async Processing**: Background processing with immediate Slack acknowledgment, then Canvas delivery

🛡️ **Error Handling**: Failed assessments send error notifications to Slack

## Filter Options

| Filter | Description | Examples |
|--------|-------------|-----------|
| `industry` | Target industry | `finance`, `healthcare`, `construction`, `retail`, `technology`, `manufacturing` |
| `tags` | Asset tags to filter by | `PII`, `SOX`, `HIPAA`, `PHI`, `Confidential` |
| `connections` | Specific connections | `snowflake`, `postgres`, `tableau`, `databricks` |
| `certificate` | Certification status | `VERIFIED`, `DRAFT`, `DEPRECATED` |
| `asset_type` | Asset types | `Table`, `Column`, `Dashboard` |

## MCP Integration

The application uses real Atlan MCP tools when available:

1. **Real MCP**: Uses `atlan:search_assets_tool` for live data
2. **Demo Mode**: Falls back to realistic demo data based on `dsm.atlan.com`  
3. **Error Handling**: Always generates assessments even if MCP fails

### Confirmed Working with dsm.atlan.com

✅ Retrieved 20+ real tables from Snowflake, Databricks, Athena
✅ Found real connections (dbt-food-beverage, prod-lakehouse, etc.)
✅ Processed actual governance metadata (certificates, owners, usage)

## Canvas Assessment Output

The system generates professional Canvas-style assessments including:

- **Health Score** (0-100) with industry benchmarking
- **Current State Analysis** with specific metrics  
- **Strategic Recommendations** with ROI projections
- **30-60-90 Day Roadmaps**
- **Business Impact Analysis**
- **Immediate Next Steps**

## Example Slack Output

After running `/atlan-health "TechCorp" https://dsm.atlan.com industry:technology tags:Finance`, you'll receive:

1. **Immediate Response**: "Processing Real Atlan Data..."
2. **Canvas Assessment**: Complete professional deliverable sent back to Slack in formatted chunks

## Development

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally  
python api/index.py

# Test locally
curl -X POST http://localhost:8080/slack/atlan-setup \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'text=TestCorp https://dsm.atlan.com industry:technology'
```

### Environment Variables

- `PORT` - Server port (default: 8080)

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Slack App     │────│  Vercel Flask    │────│  Atlan MCP      │
│   /atlan-health │    │  Health Checker  │    │  Search Tools   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌────────▼────────┐             │
         │              │ Background      │             │
         │              │ Processing      │◄────────────┘
         │              │ & Canvas Gen    │
         │              └────────┬────────┘
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌──────────────────┐
│ Immediate       │    │ Canvas Assessment│
│ Slack Response  │    │ Delivered to     │
│                 │    │ Slack Channel    │
└─────────────────┘    └──────────────────┘
```

1. **Slack Command** triggers webhook to Vercel
2. **Flask App** parses command and sends immediate response  
3. **Background Thread** fetches real Atlan data via MCP
4. **Health Assessment** calculates industry-specific scores
5. **Canvas Generation** creates professional deliverable
6. **Slack Delivery** sends Canvas back to Slack channel

## Professional Use Cases

Perfect for:
- 🎯 **Sales Teams** - Generate instant customer assessments
- 💼 **Customer Success** - Health check existing customers  
- 🏗️ **Solutions Engineering** - Technical discovery calls
- 📊 **Data Consultants** - Professional deliverables

## Version History

- **v2.2.0** - **FIXED: Canvas assessments now delivered to Slack**
- **v2.1.0** - Real Atlan MCP integration  
- **v2.0.0** - Professional Canvas assessments
- **v1.0.0** - Basic Slack integration

## Support

For questions or issues:
1. Check the `/test` endpoint for system status
2. Review logs for MCP integration status  
3. Test with `dsm.atlan.com` for demo data
4. Use `test_slack_integration.py` to verify Slack delivery

**The Canvas assessments are now delivered directly to Slack! 🎉**
