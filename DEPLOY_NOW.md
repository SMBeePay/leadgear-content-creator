# Deploy to Vercel + Railway in 10 Minutes ⚡

## Quick Start (Fastest Path to Live URL)

### Step 1: Deploy Backend to Railway (5 minutes)

1. **Go to Railway**: https://railway.app/new
2. **Sign in with GitHub**
3. **Click "Deploy from GitHub repo"**
4. **Select**: `leadgear-content-creator`
5. **Configure**:
   - Service name: `leadgear-backend`
   - Root Directory: `backend`
   - Click "Deploy"

6. **Add Environment Variables** (click Variables tab):
   ```bash
   JWT_SECRET=<paste-output-of: openssl rand -hex 32>
   FRONTEND_URL=https://your-app.vercel.app  # (update after Vercel deploy)
   DATABASE_URL=sqlite:///./data/leadgear.db  # (temporary, upgrade to Postgres later)
   REDIS_URL=redis://localhost:6379          # (temporary, add Redis service later)
   ```

7. **Copy your Railway URL**:
   - Click "Settings" → Copy the "Public Domain" URL
   - Should look like: `https://leadgear-backend.up.railway.app`
   - **SAVE THIS - you'll need it for Vercel!**

### Step 2: Deploy Frontend to Vercel (5 minutes)

**Option A: Using Vercel CLI (Faster)**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel --prod

# When prompted:
# - Set VITE_API_URL to your Railway URL (from Step 1)
```

**Option B: Using Vercel Dashboard**

1. **Go to Vercel**: https://vercel.com/new
2. **Import** your Git repository
3. **Configure**:
   - Framework Preset: **Vite**
   - Root Directory: **`frontend`**
   - Build Command: `npm run build`
   - Output Directory: `dist`

4. **Add Environment Variable**:
   - Key: `VITE_API_URL`
   - Value: `https://leadgear-backend.up.railway.app` (your Railway URL)

5. **Click "Deploy"**

6. **Wait ~2 minutes** for build to complete

7. **Copy your Vercel URL**:
   - Should look like: `https://leadgear-content-creator.vercel.app`

### Step 3: Update Backend CORS (2 minutes)

1. Go back to **Railway dashboard**
2. Click on your backend service
3. Click **Variables** tab
4. **Update** `FRONTEND_URL`:
   ```bash
   FRONTEND_URL=https://your-app.vercel.app  # Your actual Vercel URL
   ```
5. Railway will automatically redeploy

### Step 4: Test It! (1 minute)

1. **Visit your Vercel URL**: `https://your-app.vercel.app`
2. **Click "Register"** and create an account
3. **Login** with your credentials
4. **Create a project** to test the full stack

---

## 🎉 You're Live!

Your app is now deployed at:
- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-backend.up.railway.app`
- **API Docs**: `https://your-backend.up.railway.app/docs`

---

## Common Issues & Fixes

### ❌ "Network Error" when trying to login

**Problem**: Frontend can't reach backend

**Fix**:
1. Check `VITE_API_URL` is set in Vercel (Settings → Environment Variables)
2. Make sure Railway backend is running (check Railway dashboard)
3. Verify CORS is configured (should be automatic)

### ❌ "CORS Error" in browser console

**Problem**: Backend not allowing your frontend domain

**Fix**:
1. Go to Railway → Variables
2. Ensure `FRONTEND_URL` exactly matches your Vercel URL
3. Redeploy backend

### ❌ Vercel build fails

**Problem**: Build errors in frontend

**Fix**:
```bash
# Test locally first
cd frontend
npm install
npm run build

# If successful, push to git and redeploy
```

---

## Next Steps

### 1. Add a PostgreSQL Database (Recommended)

Instead of SQLite:

1. In Railway, click "New Service" → "Database" → "PostgreSQL"
2. Railway automatically sets `DATABASE_URL`
3. Redeploy backend
4. Your data will now persist properly!

### 2. Add Redis (For Background Tasks)

1. In Railway, click "New Service" → "Database" → "Redis"
2. Railway automatically sets `REDIS_URL`
3. Redeploy backend
4. Celery will now work for long-running tasks

### 3. Add API Keys (As You Get Them)

In Railway → Variables, add:
```bash
ANTHROPIC_API_KEY=sk-ant-...      # For Claude AI features
DATAFORSEO_LOGIN=...              # For keyword research
DATAFORSEO_PASSWORD=...           # For keyword research
PERPLEXITY_API_KEY=pplx-...      # For research features
```

### 4. Set Up Custom Domain (Optional)

**Vercel**:
1. Settings → Domains → Add Domain
2. Configure DNS as instructed

**Railway**:
1. Service → Settings → Domains → Add Domain
2. Configure DNS as instructed

---

## Costs

**Current Setup (Free Tier)**:
- Vercel: **Free** (100GB bandwidth/month)
- Railway: **$5 credit/month** (usually enough for testing)
- **Total**: ~$0-5/month

**With Database (Recommended)**:
- Railway PostgreSQL: Included in $5 credit for small apps
- Railway Redis: Included in $5 credit
- **Total**: Still ~$5/month for testing

---

## Monitoring Your App

**Vercel Analytics**:
- Dashboard → Your Project → Analytics
- See page views, performance, etc.

**Railway Logs**:
- Dashboard → Your Service → Deployments → View Logs
- See backend errors, API calls, etc.

**Railway Metrics**:
- Dashboard → Your Service → Metrics
- See CPU, memory, network usage

---

## Auto-Deploy Setup (Already Configured!)

Both platforms auto-deploy when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push

# Vercel and Railway will automatically deploy!
# Watch the deployments in their dashboards
```

---

## Need Help?

- **Full deployment guide**: See `DEPLOYMENT.md`
- **Architecture details**: See `IMPLEMENTATION_GUIDE.md`
- **Quick start locally**: See `QUICKSTART.md`
- **Vercel docs**: https://vercel.com/docs
- **Railway docs**: https://docs.railway.app

---

**Enjoy your live app! 🚀**

Share your Vercel URL and start testing your SEO content creation tool!
