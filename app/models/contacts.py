from app.models.database import get_db

def save_contact(name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content):
    conn = get_db()
    conn.execute('''
        INSERT INTO contacts (name, email, phone, issue, message, 
                            source, utm_source, utm_medium, utm_campaign, 
                            utm_term, utm_content)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, issue, message, 
          source, utm_source, utm_medium, utm_campaign, 
          utm_term, utm_content))
    conn.commit()

def get_lead_sources():
    db = get_db()
    sources = db.execute('''
        SELECT 
            source,
            COUNT(*) as total,
            SUM(CASE 
                WHEN created_at >= datetime('now', '-30 days') 
                THEN 1 
                ELSE 0 
            END) as last_30_days
        FROM contacts 
        GROUP BY source
        ORDER BY total DESC
    ''').fetchall()
    return sources

def get_lead_details():
    db = get_db()
    leads = db.execute('''
        SELECT 
            name,
            email,
            source,
            utm_campaign,
            utm_medium,
            created_at
        FROM contacts 
        ORDER BY created_at DESC
        LIMIT 100
    ''').fetchall()
    return leads 