# SSH Agent Forwarding Troubleshooting

## Current Issue

The SSH agent socket is mounted at `/ssh-agent` but returns "Connection refused" when trying to use it.

## Root Cause

The devcontainer was rebuilt but the docker-compose.yml wasn't updated to include the SSH agent volume mount. The mount in devcontainer.json needs to match the docker-compose setup.

## Solution: Rebuild Container Again

I've now updated **both** files:
- `devcontainer.json` (SSH agent mount + env var)
- `docker-compose.yml` (volume binding for SSH socket)

### Steps to Fix:

1. **Rebuild the container** to apply docker-compose.yml changes:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
   - Select: **"Dev Containers: Rebuild Container"**
   - Wait for rebuild

2. **Verify the fix**:
   ```bash
   # Should list your SSH keys
   ssh-add -l
   
   # Should authenticate successfully
   ssh -T git@github.com
   ```

## Alternative: Use HTTPS Instead of SSH (Temporary)

If you need to push immediately without rebuilding:

```bash
# Change remote to HTTPS
git remote set-url origin https://github.com/minimal3dp/m3dp_post_process.git

# Configure credential caching
git config --global credential.helper cache

# Push (will prompt for GitHub username + Personal Access Token)
git push
```

To create a Personal Access Token:
1. Go to https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scope: `repo` (full control)
4. Use token as password when prompted

## Why This Happened

VS Code devcontainers can mount SSH agents in two ways:
1. **devcontainer.json** `mounts` - works for some setups
2. **docker-compose.yml** `volumes` - more reliable with Podman

Both need to be configured for consistent SSH forwarding.

## After Rebuild Checklist

```bash
# 1. Check mount exists
ls -la /ssh-agent

# 2. Check environment variable
echo $SSH_AUTH_SOCK  # Should be: /ssh-agent

# 3. List keys
ssh-add -l  # Should NOT say "Connection refused"

# 4. Test GitHub
ssh -T git@github.com  # Should authenticate

# 5. Switch back to SSH remote (if using HTTPS)
git remote set-url origin git@github.com:minimal3dp/m3dp_post_process.git
```

## Prevention

After this rebuild, SSH forwarding should work persistently. The docker-compose.yml now includes the SSH agent mount as a volume binding.
