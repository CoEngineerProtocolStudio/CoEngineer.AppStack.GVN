# Co-engineer Protocol Kit: Package Status Check (v0.1.x)

 Repository is currently in a "Distributed Monorepo" state. The logic is isolated, the CI/CD is patched for the nested structure, and the package is ready for open-source consumption via GitHub Releases.

## 📦 Package Identity

* **Name:** `coengineer-appstack-gvn`
* **Engine:** Gemini 2.0 Flash + Vertex RAG
* **Architecture:** Builder Stack (Epiphany + Quick Turn)
* **Namespace:** `coengineer`

## 🚦 Status Summary

* **Source Layout:** Verified. Uses `kit/src` to prevent path pollution.
* **CI/CD Pipeline:** Active. `.github/workflows/main.yml` is configured to build from the `kit/` subdirectory and attach `.whl` artifacts to version tags.
* **Environment:** Compatible with Arch/Manjaro (local) and Streamlit Cloud (production).

## 🛠 Integration for Open-Source Users

Users can integrate this toolkit without cloning the full monorepo:

### 1. Direct Installation

```bash
# Install specific version from the Release artifact
pip install https://github.com/CoEngineerProtocolStudio/CoEngineer.AppStack.GVN/releases/download/v0.1.1/coengineer_appstack_gvn-0.1.1-py3-none-any.whl

```

### 2. Development Mode

```bash
git clone https://github.com/CoEngineerProtocolStudio/CoEngineer.AppStack.GVN.git
cd CoEngineer.AppStack.GVN
pip install -e ./kit

```

## ⚖️ Trade-off Analysis

* **Decision:** Nested `kit/` directory vs. Root-level `src/`.
* **Result:** Increased complexity in GitHub Actions (requires explicit paths), but allows the "Protocol" (Markdown) to live alongside the "Software" (Python) without mixing concerns.
* **Security:** `.gitignore` is strictly enforced to block `service-account.json` and `.env` files.

## 📝 Manifest

* [x] `pyproject.toml` (Metadata)
* [x] `main.yml` (CI/CD Fix)
* [x] `src/coengineer/` (Core Engine)
* [x] `examples/` (Reference Implementation)

**Current Version:** `v0.1.1` (Build Fix applied)
**Stability:** Alpha - Functional for Ag-Tech RAG deployments.
