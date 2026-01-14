---
description: This page explains how to enable HSTS in the appliance.
---

# Enabling HTTP Strict Transport Security (HSTS)

Open file `/etc/nginx/ipf-default/https.d/ipf-frontend.include` in your favorite text
editor and add:

```
add_header Strict-Transport-Security "max-age=31536000" always;
```

To any location that contains `add_header` config option. Final file content should look like:
```
# ---- HTML: never cache if served from /opt/ipf-frontend/html/ ----
location ~* \.html$ {
    root /opt/ipf-frontend/html/;
    add_header Cache-Control "no-cache, must-revalidate";
    add_header Strict-Transport-Security "max-age=31536000" always;
}

# ---- Cache Non-HTML static files from /opt/ipf-frontend/html/ ----
location ~* ^/(?:[^/]+|public/(?:.*/)?[^/]+)\.(?:js|css|png|jpg|jpeg|gif|ico|svg|woff2?)$ {
    root /opt/ipf-frontend/html/;
    add_header Cache-Control "public, max-age=31536000, immutable";
    add_header Strict-Transport-Security "max-age=31536000" always;
}

# ---- SPA fallback for routes without an extension ----
location / {
    include       /opt/ipf-frontend/nginx/frontend-headers;
    add_header    X-Frame-Options "DENY";
    add_header    X-Content-Type-Options "nosniff";
    add_header    X-XSS-Protection "1; mode=block";
    add_header    Strict-Transport-Security "max-age=31536000" always;

    root          /opt/ipf-frontend/html/;
    index         index.html;
    try_files     $uri /index.html;
}
```

Once configured, please run `systemctl restart nginx` to apply those configuration changes.

