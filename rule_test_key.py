veGameService.setAccessKey("AKLTYzg1N2UxxxNTFmZjxxNDk2ZmE1xxFjMDhiZTc");

        gzip_buffers 16 64k;
        gzip_http_version 1.1;
        gzip_comp_level 9;
        gzip_types text/plain text/javascript application/javascript image/jpeg image/gif image/png application/font-woff application/x-javascript text/css application/xml;
        gzip_vary on;
        proxy_pass http://127.0.0.1:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_add
veGameService.setSecretKey("WmpNd01xxxpaVGxqWXpJxxxm1PVGhoWmpFek9XRxxxdRNU5ETQ==");
