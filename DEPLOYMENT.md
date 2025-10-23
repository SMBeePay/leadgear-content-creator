# Deployment Guide - Vercel + Railway

This guide will walk you through deploying the Lead Gear Content Creator to production.

**Architecture:**
- **Frontend**: Vercel (free tier)
- **Backend**: Railway (free tier - $5 credit/month)
- **Database**: Railway PostgreSQL (free tier) or SQLite (temporary)
- **Redis**: Railway Redis (free tier)

---

## Prerequisites

1. GitHub account (for connecting to Vercel/Railway)
2. Vercel account (sign up at https://vercel.com)
3. Railway account (sign up at https://railway.app)

---

## Part 1: Deploy Backend to Railway

### Step 1: Create Railway Account & Project

1. Go to https://railway.app and sign in with GitHub
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account and select `leadgear-content-creator`
5. Railway will detect the Dockerfile

### Step 2: Configure Railway Services

You'll need to set up 3 services in Railway:

#### Service 1: Backend (FastAPI)

1. In Railway dashboard, click "New Service" → "GitHub Repo"
2. Select your repository
3. Set **Root Directory**: `backend`
4. Railway will auto-detect the Dockerfile

**Environment Variables** (click Variables tab):
```bash
# Required
JWT_SECRET=<generate-with-openssl-rand-hex-32>
DATABASE_URL=postgresql://<will-be-set-by-postgres-service>
REDIS_URL=redis://<will-be-set-by-redis-service>

# API Keys (add as you get them)
ANTHROPIC_API_KEY=sk-ant-...
PERPLEXITY_API_KEY=pplx-...
DATAFORSEO_LOGIN=...
DATAFORSEO_PASSWORD=...
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...

# URLs (update after frontend deployment)
FRONTEND_URL=https://your-app.vercel.app
BACKEND_URL=${RAILWAY_PUBLIC_DOMAIN}

# Optional
ENVIRONMENT=production
```

**Important**: Copy the **Public Domain** URL (e.g., `https://your-app.up.railway.app`) - you'll need this for Vercel!

#### Service 2: PostgreSQL Database

1. Click "New Service" → "Database" → "PostgreSQL"
2. Railway will automatically set `DATABASE_URL` environment variable
3. The backend service will automatically have access to this

**Or use SQLite temporarily** (not recommended for production):
```bash
# In backend environment variables
DATABASE_URL=sqlite:///./data/leadgear.db
```

#### Service 3: Redis

1. Click "New Service" → "Database" → "Redis"
2. Railway will automatically set `REDIS_URL` environment variable
3. The backend service will use this for Celery

#### Service 4: Celery Worker (Optional - for background tasks)

1. Click "New Service" → "GitHub Repo" (same repo)
2. Set **Root Directory**: `backend`
3. Set **Custom Start Command**: `celery -A tasks.celery_app worker --loglevel=info`
4. Add same environment variables as backend

### Step 3: Test Backend

1. Visit your Railway backend URL: `https://your-app.up.railway.app/docs`
2. You should see the FastAPI Swagger documentation
3. Try the health check: `https://your-app.up.railway.app/health`

---

## Part 2: Deploy Frontend to Vercel

### Step 1: Prepare Frontend

The frontend is already configured with `vercel.json`. Let's verify the environment variable handling:

```bash
# Make sure this file exists
cat frontend/.env.production
```

### Step 2: Deploy to Vercel

**Option A: Vercel CLI (Fastest)**

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name: leadgear-content-creator
# - In which directory is your code? ./frontend
# - Override settings? No

# After preview deployment, deploy to production
vercel --prod
```

**Option B: Vercel Dashboard (Recommended for first deployment)**

1. Go to https://vercel.com/new
2. Import your Git repository
3. Configure project:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

4. **Add Environment Variables**:
   - Click "Environment Variables"
   - Add: `VITE_API_URL` = `https://your-backend.up.railway.app` (from Railway)

5. Click "Deploy"

### Step 3: Update Backend CORS

After Vercel deployment, update your Railway backend environment variables:

```bash
# In Railway backend service, add:
FRONTEND_URL=https://your-app.vercel.app
```

Redeploy the backend service in Railway.

---

## Part 3: Connect Everything

### Update Environment Variables

**Vercel (Frontend):**
```bash
VITE_API_URL=https://your-backend.up.railway.app
```

**Railway (Backend):**
```bash
FRONTEND_URL=https://your-app.vercel.app
BACKEND_URL=https://your-backend.up.railway.app
```

### Test the Full Stack

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Register a new account
3. Create a project
4. Verify API calls work (check browser console for errors)

---

## Part 4: Custom Domain (Optional)

### Add Custom Domain to Vercel

1. In Vercel dashboard → Settings → Domains
2. Add your domain: `app.yourdomain.com`
3. Follow DNS configuration instructions
4. Vercel will auto-generate SSL certificate

### Add Custom Domain to Railway (Optional)

1. In Railway service → Settings → Domains
2. Add custom domain: `api.yourdomain.com`
3. Configure DNS as instructed
4. Update `VITE_API_URL` in Vercel to use new domain

---

## Troubleshooting

### CORS Errors

**Symptom**: Frontend can't connect to backend, CORS errors in browser console

**Fix**:
1. Verify `FRONTEND_URL` is set correctly in Railway backend
2. Check `VITE_API_URL` is set correctly in Vercel
3. Ensure both are using HTTPS (not HTTP)
4. Check Railway logs: `railway logs`

### Database Connection Errors

**Symptom**: Backend crashes with database errors

**Fix**:
1. Ensure PostgreSQL service is running in Railway
2. Check `DATABASE_URL` is set automatically
3. View Railway logs for detailed error messages

### API Not Found (404)

**Symptom**: Frontend shows "API not found" or network errors

**Fix**:
1. Verify backend is deployed and running on Railway
2. Check Railway backend URL is accessible: `https://your-backend.up.railway.app/health`
3. Verify `VITE_API_URL` in Vercel matches Railway backend URL exactly
4. Check Vercel deployment logs for build errors

### Frontend Build Fails

**Symptom**: Vercel build fails

**Fix**:
```bash
# Test build locally first
cd frontend
npm install
npm run build

# Check for TypeScript errors
npm run lint
```

---

## Production Checklist

Before going live with real users:

- [ ] Change JWT_SECRET to a secure random value
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up proper error tracking (Sentry)
- [ ] Configure Redis for production
- [ ] Set up database backups
- [ ] Add all required API keys
- [ ] Test all features end-to-end
- [ ] Set up monitoring/alerts
- [ ] Configure rate limiting
- [ ] Review security settings

---

## Cost Estimate

**Free Tier (Good for MVP testing):**
- Vercel: Free (100GB bandwidth, unlimited deployments)
- Railway: $5 credit/month (usually enough for small apps)
- Total: **$0-5/month**

**Production (Recommended):**
- Vercel Pro: $20/month (better performance, analytics)
- Railway: ~$10-20/month (depending on usage)
- Total: **~$30-40/month**

---

## Quick Deploy Commands

**Deploy frontend to Vercel:**
```bash
cd frontend
vercel --prod
```

**View Railway logs:**
```bash
railway logs
```

**Redeploy Railway backend:**
```bash
# Push to main branch, Railway auto-deploys
git push origin main
```

---

## Environment Variables Reference

### Vercel (Frontend)
| Variable | Example | Required |
|----------|---------|----------|
| `VITE_API_URL` | `https://api.railway.app` | ✅ Yes |

### Railway Backend
| Variable | Example | Required |
|----------|---------|----------|
| `JWT_SECRET` | `<random-32-char-hex>` | ✅ Yes |
| `DATABASE_URL` | Auto-set by Railway | ✅ Yes |
| `REDIS_URL` | Auto-set by Railway | ✅ Yes |
| `FRONTEND_URL` | `https://app.vercel.app` | ✅ Yes |
| `ANTHROPIC_API_KEY` | `sk-ant-...` | For AI features |
| `DATAFORSEO_LOGIN` | `email@example.com` | For keyword research |
| `DATAFORSEO_PASSWORD` | `password` | For keyword research |
| `PERPLEXITY_API_KEY` | `pplx-...` | For research |
| `GOOGLE_CLIENT_ID` | `...apps.googleusercontent.com` | For Google APIs |
| `GOOGLE_CLIENT_SECRET` | `GOCSPX-...` | For Google APIs |

---

## Next Steps After Deployment

1. **Test with real data**: Create projects, test workflows
2. **Add API keys**: As you get access to DataForSEO, Claude, etc.
3. **Monitor usage**: Check Railway usage dashboard
4. **Implement remaining features**: Follow IMPLEMENTATION_GUIDE.md
5. **Set up CI/CD**: Auto-deploy on git push (already enabled!)

---

**Your app is live! Share the Vercel URL and start testing! 🚀**
