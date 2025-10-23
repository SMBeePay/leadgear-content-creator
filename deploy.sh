#!/bin/bash

echo "🚀 Lead Gear Content Creator - Quick Deploy Script"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}Choose deployment option:${NC}"
echo "1. Deploy Frontend to Vercel"
echo "2. Deploy Backend to Railway"
echo "3. Deploy Both"
echo "4. Check deployment status"
echo ""

read -p "Enter choice (1-4): " choice

case $choice in
  1)
    echo -e "${GREEN}Deploying Frontend to Vercel...${NC}"
    cd frontend
    vercel --prod
    cd ..
    ;;
  2)
    echo -e "${GREEN}Deploying Backend to Railway...${NC}"
    echo -e "${YELLOW}Note: Make sure you've connected your repo to Railway first${NC}"
    echo "Visit: https://railway.app/new"
    echo ""
    echo "Push to main branch to trigger Railway deployment:"
    git push origin main
    ;;
  3)
    echo -e "${GREEN}Deploying both Frontend and Backend...${NC}"
    echo -e "${BLUE}Step 1: Deploy Frontend to Vercel${NC}"
    cd frontend
    vercel --prod
    cd ..
    echo ""
    echo -e "${BLUE}Step 2: Push to trigger Railway backend deployment${NC}"
    git push origin main
    ;;
  4)
    echo -e "${BLUE}Checking deployment status...${NC}"
    echo ""
    echo "Frontend (Vercel):"
    cd frontend
    vercel ls
    cd ..
    echo ""
    echo "Backend (Railway):"
    echo "Visit: https://railway.app/dashboard"
    ;;
  *)
    echo -e "${YELLOW}Invalid choice${NC}"
    ;;
esac

echo ""
echo -e "${GREEN}Done! 🎉${NC}"
echo ""
echo "Next steps:"
echo "1. Set environment variables in Vercel dashboard"
echo "2. Set environment variables in Railway dashboard"
echo "3. Test your deployment at your Vercel URL"
echo ""
echo "See DEPLOYMENT.md for detailed instructions"
