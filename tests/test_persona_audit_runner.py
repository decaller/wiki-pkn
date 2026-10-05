import unittest
from scripts.run_persona_audit import safe_url, extract, validate_round

class PersonaAuditTests(unittest.TestCase):
    def test_host_boundary(self):
        self.assertIsNone(safe_url('https://evil.test/'))
        self.assertIsNone(safe_url('http://wikipkn.insanmustaqbal.or.id/'))
        self.assertIsNone(safe_url('https://wikipkn.insanmustaqbal.or.id:444/'))
        self.assertEqual(safe_url('/abc#x'), 'https://wikipkn.insanmustaqbal.or.id/abc')

    def test_article(self):
        text, links = extract('<nav>noise</nav><article><h1>Judul</h1><p>Bukti nyata</p><a href="/abc">Baca</a></article>', 'https://wikipkn.insanmustaqbal.or.id/')
        self.assertIn('Bukti nyata', text)
        self.assertNotIn('noise', text)
        self.assertEqual(links[0], 'https://wikipkn.insanmustaqbal.or.id/abc')

    def test_quote_validation(self):
        item = {'persona':'01a','round':1,'questions':[{'question':'Q','criteria':['C'],'answer':'A','suitability':2,'completeness':2,'reason':'R','citations':[{'url':'u','quote':'fake'}]}]*4,'followups':[],'learned':[], 'recommendations':[]}
        with self.assertRaises(ValueError):
            validate_round(item, {'u':{'text':'real'}})
