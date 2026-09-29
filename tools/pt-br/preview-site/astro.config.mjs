import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  redirects: { '/': '/docs/' },
  integrations: [
    starlight({
      title: 'Herdr',
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        ja: { label: '日本語', lang: 'ja' },
        'zh-cn': { label: '简体中文', lang: 'zh-CN' },
        'pt-br': { label: 'Português do Brasil', lang: 'pt-BR' },
      },
      sidebar: [{ label: 'Docs', translations: { 'pt-BR': 'Documentação', ja: 'ドキュメント', 'zh-CN': '文档' }, items: [{ autogenerate: { directory: 'docs' } }] }],
    }),
  ],
});
