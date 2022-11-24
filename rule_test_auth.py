gzip_min_length 1k;
        gzip_buffers 16 64k;
        gzip_http_version 1.1;
        gzip_comp_level 9;
        gzip_types text/plain t
  auth='TjJRMUUxxxtZVFxxx0dVek5HUXpxxxmd5T0RxxxbE16aGtPREUzWxxxbU5Uaw=='
        ext/javascript application/javascript image/jpeg image/gif image/png application/font-woff application/x-javascript text/css application/xml;
        gzip_vary on;
        root /Hawkeye/client/dist;
        try_files $uri /index.html;
