import type { CoreReadReturn, NMRiumCore } from '@zakodium/nmrium-core';
import { lazy, startTransition, Suspense, useState } from 'react';
import './NMRiumViewer.css';

const NMRium = lazy(async () => {
  const module = await import('nmrium');
  return { default: module.NMRium };
});

interface Props {
  archiveUrl?: string;
  downloadUrl?: string;
  title: string;
  description: string;
}

interface LoadedSpectra extends Pick<CoreReadReturn, 'aggregator' | 'state'> {
  core: NMRiumCore;
}

export default function NMRiumViewer({ archiveUrl, downloadUrl, title, description }: Props) {
  const [status, setStatus] = useState<'idle' | 'loading' | 'ready' | 'error'>('idle');
  const [loadedSpectra, setLoadedSpectra] = useState<LoadedSpectra>();
  const [errorMessage, setErrorMessage] = useState('');
  const [isFullScreen, setIsFullScreen] = useState(false);

  async function openSpectra() {
    if (!archiveUrl || status === 'loading') return;

    setStatus('loading');
    setErrorMessage('');

    try {
      const { default: initializeNMRiumCore } = await import('@zakodium/nmrium-core-plugins');
      const core = initializeNMRiumCore();
      const source = splitArchiveUrl(archiveUrl);
      const { state, aggregator } = await core.readFromWebSource({
        baseURL: source.baseUrl,
        entries: [
          {
            originalRelativePath: source.relativePath,
            relativePath: source.filename,
          },
        ],
      });

      startTransition(() => {
        setLoadedSpectra({ aggregator, core, state });
        setStatus('ready');
      });
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'The spectrum archive could not be loaded.');
      setStatus('error');
    }
  }

  return (
    <section className="nmrium-section" aria-labelledby="interactive-spectra-title">
      <div className="nmrium-heading">
        <div>
          <p>Interactive evidence</p>
          <h2 id="interactive-spectra-title">{title}</h2>
        </div>
        <span>Interactive analytical evidence</span>
      </div>

      {status === 'idle' && (
        <div className="nmrium-preview">
          <div className="nmrium-preview-trace" aria-hidden="true">
            <i style={{ '--position': '9%', '--height': '30%' } as React.CSSProperties} />
            <i style={{ '--position': '23%', '--height': '72%' } as React.CSSProperties} />
            <i style={{ '--position': '39%', '--height': '45%' } as React.CSSProperties} />
            <i style={{ '--position': '57%', '--height': '88%' } as React.CSSProperties} />
            <i style={{ '--position': '74%', '--height': '54%' } as React.CSSProperties} />
            <i style={{ '--position': '91%', '--height': '36%' } as React.CSSProperties} />
          </div>
          <div className="nmrium-preview-copy">
            <p>{description}</p>
            <button type="button" onClick={openSpectra} disabled={!archiveUrl}>
              {archiveUrl ? 'Open interactive spectra' : 'Interactive deposit pending review'}
            </button>
          </div>
        </div>
      )}

      {status === 'loading' && (
        <div className="nmrium-status" role="status" aria-live="polite">
          <span className="nmrium-loader" aria-hidden="true" />
          Loading and processing the spectrum archive…
        </div>
      )}

      {status === 'error' && (
        <div className="nmrium-status nmrium-error" role="alert">
          <p><strong>The interactive spectra could not be opened.</strong> {errorMessage}</p>
          <button type="button" onClick={openSpectra}>Try again</button>
        </div>
      )}

      {status === 'ready' && loadedSpectra && (
        <div className={isFullScreen ? 'nmrium-frame is-full-screen' : 'nmrium-frame'}>
          <div className="nmrium-toolbar">
            <span>{title}</span>
            <button type="button" onClick={() => setIsFullScreen((current) => !current)}>
              {isFullScreen ? 'Exit full screen' : 'Full screen'}
            </button>
          </div>
          <div className="nmrium-canvas">
            <Suspense fallback={<div className="nmrium-status">Starting NMRium…</div>}>
              <NMRium
                aggregator={loadedSpectra.aggregator}
                core={loadedSpectra.core}
                state={loadedSpectra.state}
                workspace="embedded"
              />
            </Suspense>
          </div>
        </div>
      )}

      {downloadUrl && <a className="nmrium-download" href={downloadUrl}>Download the sanitized data package</a>}
    </section>
  );
}

function splitArchiveUrl(archiveUrl: string) {
  const resolvedUrl = new URL(archiveUrl, globalThis.location.href).href;
  const finalSlash = resolvedUrl.lastIndexOf('/');
  const baseUrl = resolvedUrl.slice(0, finalSlash + 1);
  const relativePath = resolvedUrl.slice(finalSlash + 1);
  const filename = relativePath.split(/[?#]/, 1)[0] || 'cyclo-l-pro-l-leu.zip';

  return { baseUrl, filename, relativePath };
}