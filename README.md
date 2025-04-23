# LibreTranslate Proxy with Multi-Key Auth (Python)

ระบบ proxy สำหรับแปลภาษาด้วย LibreTranslate พร้อมตรวจสอบ Authorization ด้วยหลาย API Key

## วิธีใช้งาน

1. ติดตั้ง Docker และ Docker Compose
2. รันคำสั่ง:
   ```bash
   docker-compose up --build
   `

## ตัวอย่าง Request

```json
POST /translate
Authorization: Bearer my-secret-key
Content-Type: application/json

{
  "q": "Hello world",
  "source": "en",
  "target": "th",
  "format": "text"
}
```
