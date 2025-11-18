# Atlan Slack Health Checker - Professional Data Governance Assessments

A professional Flask application that integrates with Slack to provide instant Atlan data governance health assessments using real MCP (Model Context Protocol) integration.

## Features

✅ **Real Atlan MCP Integration** - Fetches live data from Atlan tenants
🏥 **Professional Health Scoring** - Industry-specific governance assessments  
📊 **Canvas-Style Deliverables** - Client-ready assessment documents
🎯 **Industry-Specific Analysis** - Finance, Healthcare, Construction, Retail, Technology, Manufacturing
💰 **ROI Projections** - Business impact calculations and roadmaps

## Quick Start

### 1. Deploy to Vercel

```bash
# Clone and deploy
git clone <your-repo>
cd atlan-slack-health-checker
vercel deploy
```

### 2. Test the API

**Base URL:** `https://your-app-name.vercel.app`

**Health Check:**
```bash
curl https://your-app-name.vercel.app/
```

**Test Endpoint:**
```bash
curl https://your-app-name.vercel.app/test
```

### 3. Test Health Check Directly

```bash
curl -X POST https://your-app-name.vercel.app/slack/atlan-setup \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'text=TechCorp https://dsm.atlan.com industry:technology tags:PII,Customer&user_name=testuser&channel_name=general'
```

## Slack Integration

### Slack App Configuration

1. **Request URL:** `https://your-app-name.vercel.app/slack/atlan-setup`
2. **Command:** `/atlan-health` (or whatever you configure)
3. **Method:** POST

### Command Examples

```bash
# Finance Industry Assessment
/atlan-health "MegaBank Corp" https://bank.atlan.com industry:finance tags:PII,SOX

# Healthcare Assessment  
/atlan-health "Regional Hospital" https://dsm.atlan.com industry:healthcare tags:PHI,HIPAA

# Technology Company with Specific Connections
/atlan-health TechCorp https://dsm.atlan.com connections:snowflake certificate:VERIFIED

# Construction Company Assessment
/atlan-health "BuildCorp Inc" https://build.atlan.com industry:construction tags:Safety,Projects
```

## Filter Options

| Filter | Description | Examples |
|--------|-------------|-----------|
| `industry` | Target industry | `finance`, `healthcare`, `construction`, `retail`, `technology`, `manufacturing` |
| `tags` | Asset tags to filter by | `PII`, `SOX`, `HIPAA`, `PHI`, `Confidential` |
| `connections` | Specific connections | `snowflake`, `postgres`, `tableau`, `databricks` |
| `certificate` | Certification status | `VERIFIED`, `DRAFT`, `DEPRECATED` |
| `asset_type` | Asset types | `Table`, `Column`, `Dashboard` |

## MCP Integration

The application attempts to use real Atlan MCP tools when available:

1. **Real MCP**: Uses `atlan:search_assets_tool` for live data
2. **Demo Mode**: Falls back to realistic demo data based on `dsm.atlan.com`
3. **Error Handling**: Always generates assessments even if MCP fails

### MCP Functions Used

- `atlan:search_assets_tool` - Asset discovery and metadata
- `atlan:get_assets_by_dsl_tool` - Advanced querying (future)
- `atlan:traverse_lineage_tool` - Lineage analysis (future)

## Output Format

The system generates professional Canvas-style assessments including:

- **Health Score** (0-100) with industry benchmarking
- **Current State Analysis** with specific metrics
- **Strategic Recommendations** with ROI projections
- **30-60-90 Day Roadmaps** 
- **Business Impact Analysis**
- **Immediate Next Steps**

## Industry Support

| Industry | Regulations | Focus Areas | Health Multiplier |
|----------|-------------|-------------|------------------|
| Finance | SOX, PCI DSS, GDPR | Customer data, transactions | 0.85 |
| Healthcare | HIPAA, FDA 21 CFR Part 11 | Patient data, PHI | 0.80 |
| Construction | OSHA, EPA, ISO 9001 | Project data, safety | 0.90 |
| Retail | PCI DSS, GDPR, CCPA | Customer data, inventory | 0.88 |
| Technology | SOC 2, GDPR, ISO 27001 | User data, analytics | 0.92 |
| Manufacturing | ISO 9001, OSHA, EPA | Production, quality | 0.87 |

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
```

1. **Slack Command** triggers webhook to Vercel
2. **Flask App** parses command and filters
3. **MCP Integration** fetches real Atlan data
4. **Health Assessment** calculates industry-specific scores
5. **Canvas Generation** creates professional deliverable
6. **Background Processing** outputs results asynchronously

## Error Handling

- ✅ **MCP Failures** - Falls back to demo data
- ✅ **Invalid Commands** - Helpful error messages
- ✅ **Network Issues** - Graceful degradation
- ✅ **Industry Detection** - Smart defaults

## Professional Use Cases

Perfect for:
- 🎯 **Sales Teams** - Generate instant customer assessments
- 💼 **Customer Success** - Health check existing customers
- 🏗️ **Solutions Engineering** - Technical discovery calls
- 📊 **Data Consultants** - Professional deliverables

## Version History

- **v2.1.0** - Real Atlan MCP integration
- **v2.0.0** - Professional Canvas assessments
- **v1.0.0** - Basic Slack integration

## Support

For questions or issues:
1. Check the `/test` endpoint for system status
2. Review logs for MCP integration status
3. Test with `dsm.atlan.com` for demo data

Ready to generate professional data governance assessments in under 30 seconds! 🚀
